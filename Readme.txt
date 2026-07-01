Little Lemon Web Application

API Endpoints

User Registration
POST /auth/users/

Token Authentication
POST /auth/token/login/

Menu API
GET    /restaurant/menu-items/
POST   /restaurant/menu-items/
GET    /restaurant/menu-items/<id>
PUT    /restaurant/menu-items/<id>
DELETE /restaurant/menu-items/<id>

Booking API
GET    /restaurant/booking/tables/
POST   /restaurant/booking/tables/
GET    /restaurant/booking/tables/<id>/
PUT    /restaurant/booking/tables/<id>/
DELETE /restaurant/booking/tables/<id>/