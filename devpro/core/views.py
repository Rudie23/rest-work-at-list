from django.http import JsonResponse
from django.core.paginator import Paginator

from devpro.core.models import Author

DEFAULT_PAGE_SIZE = 25


def authors(request):
    page_number = request.GET.get('page', 1)
    page_size = request.GET.get('page_size', DEFAULT_PAGE_SIZE)

    queryset = Author.objects.all()
    if q := request.GET.get('q'):
        queryset = queryset.filter(name__icontains=q)

    paginator = Paginator(queryset, per_page=page_size)
    page = paginator.get_page(page_number)

    return JsonResponse(
        {
            'data': [a.to_dict() for a in page.object_list],  # No lugar de eu passar por todos os registros do banco,
            # vou passar só pelo os que foram repassados pela página
            'count': paginator.count,
            'current_page': int(page_number),
            'num_pages': paginator.num_pages
        }
    )
