from django.urls import path, include
from .views import RoomView, RoomTypeView, RoomStatusView, RoomListView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Rooms', RoomView)
router.register('RoomType', RoomTypeView)
router.register('RoomStatus', RoomStatusView)

urlpatterns = [
    path('room/', include(router.urls)),
    path('room_list/', RoomListView.as_view())
]