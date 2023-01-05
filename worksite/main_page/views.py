from django.shortcuts import render


def main_page_view(request):
    return render(request, template_name='main_page/main_page.html')
