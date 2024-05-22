from .celery import app as celery_app

__all__ = ('celery_app',)

# # from django.conf import settings
# from .mongodb.dbconnect import dbconnect

# print('outer init')


# def main():
#     pass


# if __name__ == "__main__":
#     print('INIT')
#     print('Waiting for DataBase connection... ... ...')
#     [DATABASE, COLLECTION] = dbconnect()
#     main()
