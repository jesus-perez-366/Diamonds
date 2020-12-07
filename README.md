# Diamonds

## Descripcion

Elaboracion de 4 modelos de regresion lineal para realizar la prediccion del precio de los diamantes segun diversos valores de ciertas variables presentes en un Data Set.


## Procedimiento

1.- Se estudio la informacion de la data y se realizo una limpieza de datos que pudiesen desviar los valores en la prediccion.

2.- Se normalizaron los valores numericos de las variables con la finalidad de evitar aumento en la variancia debido a la Unidad con que se encontraba las variables.

3.- Se realizo un pair plot de las variables numericas antes y despues de haber limpiado el data.

4.- Las variables categoricas se tranformaron en 0 y 1 para poder tomar encuenta su efecto en la prediccion.

5.- Desarrollo de los modelos

6.- Verificacion de la precision de cada modelo tomando como metrica "mean squared error"


## Modelo

Se desarrollaron 4 modelo:

1.- Linear Regression

2.- KNN Neighbors

3.- Random Forrest Regression

4.- Gradien Boosting Regressor



### Pairplot antes y depsues de la limpieza del Data

inicio

<img src=output/pairplotini.png width="1000">


final

<img src=output/pairplotfina.png width="1000">


### Pairplot del archivo test

<img src=output/pairplottest.png width="1000">


## Coclusiones
El mejor modelo que obtuvo la mejor metrica fue el     el cual nos dio un valor de 0,007 en el mean squared error cuando se realizo la prediccion al y_test. sin embargo al hacer la prediccion de los valores del archivo test, y realizar el summit en la competencia de Kaggle el mean squared error fue de 0,016.

El aumento del error se puede deber a que al realizar la limpiza de los datos (Eliminacion de outliers) se elimino informacion que mejoraba la prediccion para ciertos datos contenidos en archivo test, ademas al ver las imagenes anteriores se aprecia que mis datos luego de la limpiez no toma encuenta los valores dispersos en el pairplot del test y probablemente mente para esos valores es donde hubo mas error en la prediccion. por ello es muy importante hacer una manipulacion correcta del data set.
