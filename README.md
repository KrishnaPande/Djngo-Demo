# Djngo-Demo
 Practise Django Understand each aspect

HyperlinkedModelSerializer is a serializer class in Django REST Framework that uses hyperlinks to represent relationships, rather than primary keys.

It is similar to the ModelSerializer class, but it includes a url field for each related object, instead of the id field. This allows you to create more RESTful APIs, as clients can use the hyperlinks to navigate the relationships between your objects.

To use HyperlinkedModelSerializer, you simply need to subclass it from ModelSerializer and set the fields attribute to include the fields you want to serialize. For example:

from rest_framework.serializers import HyperlinkedModelSerializer

`class PostSerializer(HyperlinkedModelSerializer):

    class Meta:

        model = Post

        fields = ('id', 'title', 'author', 'content')`

This serializer will serialize the Post model, including the url field for the author and content fields.
HyperlinkedModelSerializer is a powerful tool that can help you create more RESTful APIs.

#### **ViewSet**

A ViewSet in Django REST Framework is a class that defines the actions that can be performed on a model using the API.
ViewSets are a type of class-based view that combines the logic for a set of related views in a single class. They provide a way to perform CRUD (Create, Read, Update, Delete) operations on a model using the API.
There are four types of ViewSets in Django REST Framework:
ViewSet
GenericViewSet
ReadOnlyModelViewSet
ModelViewSet
ViewSet is the most basic type of ViewSet. It does not provide any method handlers, such as .get() or .post(). Instead, it provides actions, such as .list() and .create().
GenericViewSet is a subclass of ViewSet that provides a set of generic actions, such as .list(), .create(), .retrieve(), .update(), and .destroy().
ReadOnlyModelViewSet is a subclass of GenericViewSet that only allows for read operations, such as .list() and .retrieve().
ModelViewSet is a subclass of GenericViewSet that allows for all operations, such as .list(), .create(), .retrieve(), .update(), and .destroy().
ViewSets are a powerful tool that can help you create RESTful APIs quickly and easily.

Viewsets are a powerful tool in Django REST Framework that can help you create RESTful APIs quickly and easily. Here are some of the reasons why you should use viewsets:
They simplify the process of creating API endpoints.
Viewsets provide a set of ready-made methods that you can use to perform CRUD operations on a model. This saves you time and effort, and allows you to focus on the functionality of your API.
They make your code more consistent.
Viewsets enforce a consistent URL configuration for your API. This makes it easier for clients to navigate your API and understand how it works.
They can be used with routers.
Routers are a way to organize your API endpoints and make them easier to manage. Viewsets can be used with routers to create a well-organized and easy-to-use API.
They are extensible.
Viewsets can be extended to add custom functionality. This makes them a flexible and adaptable solution for your API needs.
If you are looking for a way to create RESTful APIs quickly and easily, viewsets are a great option. They are a powerful tool that can help you create consistent, well-organized, and extensible APIs.

#### **Router**

A Router in Django REST Framework is a class that helps you define the URLs for your API. It takes care of generating the URLs for all of the actions that are available for your views.
Routers are a great way to organize your API endpoints and make them easier to manage. They can also be used to generate URLs for related objects, which can be helpful for creating nested APIs.
There are three main types of routers in Django REST Framework:
1. DefaultRouter
2. SimpleRouter
3. Custom Router
DefaultRouter is the most basic type of router. It provides a set of default URLs for all of the actions that are available for your views.
SimpleRouter is a subclass of DefaultRouter that provides a more limited set of URLs. This is useful if you only need to expose a subset of the actions that are available for your views.
Custom Router is a subclass of Router that allows you to define your own URLs. This is useful if you need to create a custom URL structure for your API.
Routers are a powerful tool in Django REST Framework that can help you create well-organized and easy-to-use APIs.

#### **Routing**

Routing in Django is the process of determining which view function to call based on the requested URL. It is done using the URL dispatcher, which is a part of the Django web framework.
The URL dispatcher is a table that maps URLs to view functions. When a request is made to the Django web server, the URL dispatcher looks up the URL in the table and calls the corresponding view function. The view function then processes the request and returns a response.
URL patterns are used to define the URLs that are mapped to view functions. URL patterns are strings that are used to match requested URLs. They can contain regular expressions to match specific parts of the URL.
There are two main ways to define URL patterns in Django:
Using the urls.py file
Using decorators
The urls.py file is a Python file that is located in the root of your Django project. It contains a list of URL patterns that are used to map URLs to view functions.
Decorators are a way to define URL patterns that are associated with a specific view function. Decorators are functions that are used to modify the behavior of other functions. They can be used to define URL patterns that are associated with a specific view function.
Routing in Django is a powerful feature that allows you to define the URLs that are used to access your website. It is a flexible feature that can be used to create a variety of URL structures.