/* 
Curso de Introduccion a C#
## Dif Versiones de .NET
    NET Framework (4.8) = Apicaciones solo para Windows
    NET Core (3.1) = Version OpenSource que es multiplataforma.
    NET 5 (y luego la 6) = Version más reciente que unifica .Net Core con .NET Framework, opensource y multiplataforma
*/


using System; /*namespace predefinido por el lenguaje
                consta de un conjunto de instrucciones*/



namespace holaMundo
{
/*NameSpace: Sirve para crear un bloque, y que todas 
las funciones del mismo se encuentren asociadas
al bloque en cuestion. Es como C# va a identificar
diferentes partes de un programa 


Los namespaces es como C# se va a organizar
Tiene que ser unico en todo el codigo C# que se va 
a tener. Dividir c/u de las partes que se van a 
tener en el programa

NameSpace
    - Clases
        - Metodos




Tipos de datos:
int
string
bool
float
double


Operadores logicos:
And : &&
Or : || 
Not : !


Buena practica es hacer operaciones (+,*,/,-) entre mismos tipos de datos. 



La diferencia entre Arreglos y listas es que el tamaño del Arreglo es estatico, mientras que el tamaño de la
Lista es dinamico.


0 para True
1 para False
*/
    
    
    class Program //Clase ppal del programa
    {
        static void Main(string[] args)
        {
            
            Console.WriteLine("Please state your name");
            var name = Console.ReadLine(); //Leer info de la terminal
            Console.WriteLine(name.GetType()); //Por default el readline es string
            Console.WriteLine("Please state your age!");
            int age = Convert.ToInt32(Console.ReadLine()); //cast a otro tipo de datos
            Console.WriteLine("Hi! " + name); //print statement
            Console.WriteLine("You're {0} years old", age); //print statement
            var lastName = "Lopez"; //C# castea al mejor tipo de dato para almacenar el dato.
            //concatenacion de String
            string information = "The information you requested was: \nName: " + name + "\nLast name: " + lastName + "\nAge: " + age; 
            Console.WriteLine(information);
            


            //Arreglos: Estaticas
            double[] itemsValues = new double [100]; //1era forma de declarar arreglos
            string[] itemsNames = new string[] {"Dog Teddy", "Cat Teddy", "C# Hoodie"}; //2nda de forma de declarar arreglos 



            //Listas: Dinamicas
            List<string> foodNames = new List<string>(); //declaracion de una lista
            foodNames.Add("Bandeja Paisa"); //añadir item a la lista
            foodNames.Count(); //Longitud de la lista
            foodNames.ForEach(); //realizar accion especifica x c/u de los elementos de la lista
            foodNames.Remove("Bandeja Paisa"); //quitar elemento de la lista x nombre
            foodNames.RemoveAt(0); //quitar elemento de la lista x indice 


            //Ciclos
            int i;
            foreach (var name in itemsNames)
            {
                Console.WriteLine(name);
            }
            for (i = 0; i < itemsNames.Length; i++)
            {
                Console.WriteLine(itemsNames[i]);
            }
            i = 0;
            while (i < itemsNames.Length)
            {
                Console.WriteLine(itemsNames[i]);
                i++;
            }
            do
            {
                Console.WriteLine(itemsNames[i]);
                i++;
            } while (i < itemsNames.Length);

        
            //Objetos
            Random rand = new Random();
            rand.Next(1,10); //invacacion de metodos de objetos


            //Condicionales
            if(age == 18){Console.WriteLine("Mayor de edad");}


            switch(age)
            {
                case 18:
                    Console.WriteLine("Mayor de edad");
                    break;
                default:
                    Console.WriteLine("No se");
                    break;
            }
        }
    }

}
