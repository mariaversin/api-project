Api-Project

El proyecto consistía en crear una API mediante bottle, conectando con una base de datos, en mi caso, con MongoDB Atlas. 
Lo primero que hice fue crearme una cuenta en MongoDB Atlas, y subí un json con toda la información de las conversaciones, que más tarde iba a analizar. EN segundo lugar, en un visual code, fui desarrollando los endpoints de la API, tanto con get como con post:

 - (POST) `/user/create`: Crear un nuevo usuario.

 - (GET) `/chat/create`: Crear un nuevo chat.

 - (GET) `/chat/<chat_id>/adduser`: Añadir un usuario a un chat especificado.

 - (POST) `/chat/<chat_id>/addmessage`: Añadir un mensaje a la conversación.

 - (GET) `/chat/<chat_id>/list`: Sacar todos los mensajes, en función del 'chat id' ingresado.

 - (GET) `/chat/<chat_id>/sentiment`: En este punto, había que hacer una análisis de sentimiento, sacando los token de los textos y hacer un estudio de cada chat (si era positivo, negativo o neutro).


