## Agenda

*En este archivo se encuentra la aplicación de la agenda y sus componentes estéticos que se encuentran en la carpeta templates.*

  

En urls.py se pueden encontrar las ubicaciones a las que se pueden accedeer desde esta aplicación

  

En views.py se ve el webrequest que solicita la aplicación cuando se le accede

  

Usamos el siguiente template: https://colorlib.com/wp/template/calendar-19/

  

Para agendar reuniones nos vamos a la sección de admin, seleccionanos "add agendar" y agendamos una reunión, esto no está conectado a la pantalla, pero sí a la base de datos.

  

De la misma forma podemos agendar reuniones escribiéndolas en el código, esto lo podemos hacer yendonos a templates>agenda>agenda.html y bajo var Calendar escribimos la reunión, respetando el formato que se puede ver, esta opción no está conectada a la base de datos, pero sí despliega en pantalla las reuniones agendadas de esta forma.