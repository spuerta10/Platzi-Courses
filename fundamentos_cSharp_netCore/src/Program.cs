/*
Para C# todo es un objeto
todo hereda los atributos de la clase
object

Atajo de teclado cw para imprimir por pantalla


Arreglos vs. Colecciones 
Usar arreglos para mejorar performance y
en casos de alto uso del procesador
Colecciones especializadas para manejo de ciertas
cosas, tamaño flexible

Colecciones 
Simples {
    Guarda objetos; 
    operaciones de boxing : crear una caja para transformar el  objeto al tipo de dato de la coleccion
    y unboxing : deshacer la caja para transformar el objeto al tipo de dato de que era anteriormente
} 
Especializadas : Colecciones para manejar tipos de datos especificos
Genericas : Colecciones para guardar objetos especificos sin necesidad del boxing y unboxing 
Concurrentes : Colecciones para trabajar con multiparalelismo 


Cada objeto tiene un hashCode unico, creado a la hora de la instanciacion 


Poner varias lineas en comentario : ctrl + k + c 
Quitar varias lines de comentario : ctrl + k + u


El constructor tiene que ser lo mas rapido posible, para esto idealmente deberia de estar desconectado
de procesos de entrada y salida de datos (conexiones a BD, lectura de archivos y demas)


Crear un metodo encargado de incializar todo los valores del programa


Por convencion la carpeta app contien el motor de la aplicacion, el modulo donde esta la logica de la aplicacion;
la carpeta util contiene multiples utilidades como por ejemplo formatos o separadores a imprimir.

Clases estaticas : No permite crear nuevas instancias, pero si invocar sus metodos.

Si un metodo o clase tiene mas de 50 lineas probablmente esta mal diseñado, un metodo o clase deben de tener un unica responsabilidad

Refactoring: Mover funcionalidades de una parte del programa a otra

*/

using Objects.Escuela;
using System.Linq;

namespace Main
{
    class Program
    {
        static void Main(string[] args)
        {
            var escuela = new Escuela(año: 1991, nombre: "CSI"); //asignacion de parametros creacion de objeto
            var escuela2 = new Escuela()
            {
                Nombre = "UPB", //set de propiedad Nombre de la escuela

            };
            escuela.tipoEscuela = TipoEscuela.Secundaria;
            Console.WriteLine(escuela);


            escuela = null;
            if (escuela?.Cursos != null)
            /*
            Primero chequea que la escuela no sea null, y despues cheque que Cursos no sea null
            */
            {
                System.Console.WriteLine(escuela);
            }

            var tiposEscuela = new List<TipoEscuela>(); //lista de tipos de escuela

            var intList = new List<int>() {
                301,302,303,304,305,306,307,308,308  
            };

            //delegados
            intList.RemoveAll(delegate (int num) /*
                                                    remove all recorre la lista y elimina los que cumplan la condicion
                                                    en este caso, la condicion la da el delegado
                                                    */
            {
                return num == 301;
            });

            foreach(int num in intList)
            {
                System.Console.WriteLine(num);
            }
            //expresiones lambda
            intList.RemoveAll((int num)=> num == 303 || num == 304);

            string[] nombre1 = { "Alba", "Felipa", "Eusebio", "Farid", "Donald", "Alvaro", "Nicolás" };
            string[] apellido1 = { "Ruiz", "Sarmiento", "Uribe", "Maduro", "Trump", "Toledo", "Herrera" };
            string[] nombre2 = { "Freddy", "Anabel", "Rick", "Murty", "Silvana", "Diomedes", "Nicomedes", "Teodoro" };
            /*
            C# posee sql embebido, se llama LINQ
            Ejemplo de producto cartesiano
            */
            var listaAlumnos = from n1 in nombre1
                               from n2 in nombre2
                               from a1 in apellido1
                               select $"{n1} {n2} {a1}";
        }                   
    }
}
