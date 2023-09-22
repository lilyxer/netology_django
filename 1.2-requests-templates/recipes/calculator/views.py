from django.shortcuts import render, reverse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}

def index_view(request):
    template_name = 'calculator/index.html'
    pages = {
        'Омлет': reverse('omlet'),
        'Паста': reverse('pasta'),
        'Сендвич': reverse('buter'),
        }
    context = {
        'title': 'Книга рецептов',
        'pages': pages,
               }
    return render(request, template_name, context)

def get_context(request, dishes:str) -> tuple:
    my_name = [x for x in request.path.split('/') if x][-1]
    template_name = 'calculator/menu.html'
    servings = int(request.GET.get('servings', 1))
    my_recipes = DATA.get(my_name)
    if servings > 1 and DATA.get(my_name):
        my_recipes = {key: value*servings for key, value in DATA[my_name].items()}
    page = {'Возврат на главную страницу': reverse('home')}
    context = {
        'title': f'Рецепт "{dishes}" для {servings} персон',
        'page': page,
        'recipe': my_recipes}
    return template_name, context

def omlet_view(request):
    template_name, context = get_context(request=request, dishes='омлета')
    return render(request, template_name, context)

def pasta_view(request):
    template_name, context = get_context(request=request, dishes='паста')
    return render(request, template_name, context)

def buter_view(request):
    template_name, context = get_context(request=request, dishes='сендвич')
    return render(request, template_name, context)