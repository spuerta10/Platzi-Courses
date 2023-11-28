using System;
namespace Objects.Escuela 
/* 
Los namespaces son necesarios a la hora de
importar una clase en otro modulo
*/



/*
Se encapsulan las funcionalidades que quiero generar yo
*/
{
    public class Escuela 
    {
        public string nombre;
        public string Nombre 
        {
            /* 
            Propiedad de la clase
            Las propiedades solo retornan y asignan
            a la variable que esta por detras
            */
            get { return nombre; }
            set { nombre = value.ToLower(); }

        }

        /*
        crear propiedad de la variable añoDeCreacion
        mas rapido
        */
        public int añoDeCreacion {get; private set;} //solo se puede usar el set dentro de la clase, no por fuera 

        public TipoEscuela tipoEscuela { get; set; } 

        public Escuela(string nombre, int año = 2022 /*parametro opcional, por default 2022*/)
        {
            this.nombre = nombre;
            //asignacion por medio de la propiedad
            añoDeCreacion = año;
        }

        public string[] Cursos { get; set; } //propiedad arreglo

        public List<TipoEscuela> TipoEscuela {get; set;} //propeiedad lista

        //constructor por medio de igualacion por tuplas
        public Escuela(string nombre) => (Nombre) /*propiedad*/ = (nombre);

        public Escuela(string nombre, TipoEscuela TipoEscuela)
        {   
            (Nombre, tipoEscuela) =  (nombre, TipoEscuela); //asignacion por tuplas
        }

        public Escuela(){}

        public override string ToString()
        {
            return $"Nombre: {Nombre}, Tipo: {tipoEscuela} {System.Environment.NewLine}Año: {añoDeCreacion}"; //para darle formato a String usar $
            //System.Environment.NewLine : salto de linea en cualquier sistema operativo
        }
    }
}