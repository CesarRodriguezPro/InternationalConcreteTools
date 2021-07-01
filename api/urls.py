from django.urls import path
from .views import ToolListApiView,ToolDetailApiView, ToolTypesDetailApiView, ToolTypesListApiView, UserRecordView

app_name = 'api'

urlpatterns = [
    path('', ToolListApiView.as_view(), name='tool_list'),
    path('detail/<tool_code>', ToolDetailApiView.as_view(), name='tool_detail'),
    path('type', ToolTypesListApiView.as_view(), name='type_list'),
    path('type_detail/<type_id>', ToolTypesDetailApiView.as_view(), name='type_detail'),
    path('user/', UserRecordView.as_view(), name='user' )

]