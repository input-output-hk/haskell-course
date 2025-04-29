-- Crea una función de orden superior que reciba 3 parámetros: Una función y los dos parámentros de dicha función, e 
-- invertir el orden de los parámetros. 
-- Por ejemplo: `(/) 6 2` retorna `3`. Pero: `flip' (/) 6 2` retorna `0.3333333333`


-- Crea la función `uncurry'` que convierte una función currificada en una función sobre pares. 
-- O sea, esto: `(+) 1 2` que retorna `3` puede ser escrito como `uncurry' (+) (1,2)` (con los dos argumentos adentro del par).


-- Crear la función `curry` que convierte una función no currificada en una currificada. 
-- O sea, esto: `fst (1,2)` que retorna `1` puede ser escrito como `curry' fst 1 2` (con la tupla convertida en dos argumentos diferentes).


-- Utiliza funciones de orden superior, aplicación parcial y estilo de punto-libre para crear una fucnión que chequea si una palabra contiene una letra mayúscula.
-- Comienza utilizando simplemente una función de orden superior y construye desde allí. 


-- Crea la función `contar`que recibe un equipo ("Rojo", "Azul", o "Verde") y devuelve la cantidad de votos que cada equipo tiene en `votos`.

votos :: [String]
votos = ["Rojo", "Azul", "Verde", "Azul", "Azul", "Rojo"]


-- Crea una función de una línea, que filtre `autos` por marca e indique si queda alguno disponible.

cars :: [(String,Int)]
cars = [("Toyota",0), ("Nissan",3), ("Ford",1)]
