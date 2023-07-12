import logging

from reportlab.pdfgen import canvas

from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.http import (
    HttpResponse,
    HttpRequest
)

from todo_list.models import Todo
from todo_list.forms import TodoListModelForm

logger = logging.getLogger("core")


class TodoListView(FormView):
    """
    The form method saves the user's input
    The post method specifies the status of the item or deletes the item
    The get method also downloads all
    the items from the database and returns them in the form of a PDF
    """
    template_name = "pages/todo_list.html"
    form_class = TodoListModelForm
    page_title = "Todo list"
    success_url = reverse_lazy('todo_list')

    def form_valid(self, form):
        form.save()
        logger.info("User entered content")
        return super().form_valid(form)

    @csrf_exempt
    def dispatch(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = self.page_title
        context['list_items'] = Todo.objects.order_by("created")
        return context

    def post(self, request, *args, **kwargs):
        if 'finished' in request.POST:
            todo_id = request.POST.get('finished')
            todo = get_object_or_404(Todo, id=todo_id)
            todo.status = 'complete'
            todo.save()
            logger.info(
                f"The user changed {todo.subject}'s status to complete"
            )

        elif 'deleted' in request.POST:
            todo_id = request.POST.get('deleted')
            todo = get_object_or_404(Todo, id=todo_id)
            todo.delete()
            logger.info(f"The user deleted {todo.subject}")

        return super().post(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        if 'get_tasks' in request.GET:
            tasks = Todo.objects.order_by("created")

            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = (
                'attachment; filename="TodoList.pdf"'
            )

            pdf = canvas.Canvas(response)
            y = 820  # Initial y-coordinate

            for item in tasks:
                pdf.drawString(
                    50,
                    y,
                    f"{item.priority}.    "
                    f"{item.subject}      >>>       "
                    f"{item.status}         "
                    f"{item.created.date()}"
                )
                y -= 20

            pdf.showPage()
            pdf.save()
            logger.info("The user requested a Todo list PDF file")
            return response

        return super().get(request, *args, **kwargs)
