from repositories.postgres.models import Base
from repositories.repository import Repository


def on_first_startup(repository: Repository):
    create_database(repository)
    create_categories(repository)
    # create_tags(repository)
    create_posts(repository)
    # check(repository)
   

def create_database(repository):
    Base.metadata.drop_all(repository.engine)
    Base.metadata.create_all(repository.engine)


def create_categories(repository: Repository):
    repository.tags_categories.create_category('Хакатоны') 
    repository.tags_categories.create_category('Форумы')
    repository.tags_categories.create_category('Стажировки')
    repository.tags_categories.create_category('Тестирования')


def create_tags(repository: Repository):
    repository.tags_categories.create_tag('Python')
    repository.tags_categories.create_tag('Java')
    repository.tags_categories.create_tag('')
    repository.tags_categories.create_tag('C++')
    repository.tags_categories.create_tag('C')
    repository.tags_categories.create_tag('Java')
    repository.tags_categories.create_tag('Frontend')
    repository.tags_categories.create_tag('Backend')

def create_posts_manually(repository: Repository):
    repository.posts.create(
        text = "Это стажировка для Python Backend",
        link = "htttps://google.com",
        category = "Стажировки",
        tags = ['Python', 'Backend'],
        photo = 'files/photo1.jpg'
    )

    repository.posts.create(
        text = "Это стажировка для Java Fronted",
        link = "htttps://google.com",
        category = "Стажировки",
        tags = ['Java', 'Frontend'],
        photo = 'files/photo1.jpg'
    )

    repository.posts.create(
        text = "Хакатон для дебилоа",
        link = "htttps://google.com",
        category = "Хакатоны/олимпиады",
        tags = ['Backend'],
        photo = 'files/photo1.jpg'
    )

def create_posts(repository: Repository):
    from posts import posts

    for post in posts:
        repository.posts.create(
            text=post['text'],
            photo=post['photo'],
            link=post['link'],
            tags=post['tags'],
            category=post['category']
            )


def check(repository: Repository):
    for category in repository.menu.get_categories():
        # print(category.id, category.title)
        pass

    for tag in repository.menu.get_tags_by_category(1):
        print(tag.title)