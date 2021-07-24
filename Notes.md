# Notas

- Si se usa PopMatrix, las coordinas del entorno anterior son guardas, para
volver a ponerlas en su estado original hay que usar PushMatrix.

- Si se usaPopMatrix y se intenta arreglar con Rotate y Translate no funciona.

- Cuando se usa Translate y Rotate solo afectara a los widgets que se
dibujaran, es decir, no afectara a los widgets que ya estan dibujados.

- El orden de ejecucion de las canvases es:
  - Primero, el canvas de la superclass,
  - Segundo, el canvas de la instance,
  - Tercero, el canvas.after de la superclass.

- Seria la misma logica para canvas.before?