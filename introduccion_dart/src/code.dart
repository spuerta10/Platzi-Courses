/*
En Dart se hace uso de camelCase
Dart toma el numero 0 como un numero positivo
*/

void dtypes(){
  //Tipos de datos basicos en dart
  bool i = true;
  int number = 12;
  double doub = 12.5; //tambien se pueden almacenar int con este dtype pero usa mas memoria
  String text = "Hola que mas";
  /*
  Tipo de datos dinamico, se puede cambiar su tipo de dato en tiempo de compilacion
  Dart infiere su tipo de dato. 
  */
  dynamic h = "Hola que mas";
  h = 12;
  /*
  Tipo de datos dinamico, solo para numeros, se puede cambiar su tipo de dato en tiempo de compilacion
  Dart infiere su tipo de dato ya sea int o double.
  */
  num w = 12; //int
  w = 12.5; //double
  /*
  Listas dinamicas para almacenar cualquier tipo de dato en ellas
  */
  List<int> ages = [12,13,15]; 
  List<dynamic> countries = ["Hola", 12.7, ages];
  /*
  Tipo de datos dinamico, Dart infiere su tipo de dato.
  Su tipo de dato no puede cambiar en tiempo de compilacion. 
  */
  var a = 12;
  /*
  El valor de final no tiene que ser conocido en tiempo de compilacion,
  El valor de const debe de ser conocido en tiempo de compilacion.
  Inmutables, no cambiaran en la ejecucion del programa.  
  */
  final o;
  const e = 12; //La constante debe de ser inicializada
}



void variablesOperations(){
  int age, age2;
  /*
  Incrementar o decrementar valor
  */
  age = 12;
  age2 = age++; //Primero asignacion y luego incremento
  age2 = ++age; //Primero incremento y luego asignacion
  age2 = --age; //Primero decrementoy luego asignacion
  age2 = age--; //Primero asignacion y luego decremento
}



void stringOptions(){
  /*
  Concateniacion: Unir dos strings por medio del +
  Interpolacion: Introducir un string en otro por medio del $
  */
  String interpol = "Hola que ${"mas"}";
  String concat = "Hola que " + "mas";
  interpol.toUpperCase(); //todo a mayusc
  interpol.toLowerCase(); //todo a minusc
  interpol.replaceAll("H", "A"); //reemplazar caracteres especificos
} 



void cast(){
  //Casteos de diferentes tipos de datos
  //String a numnericos
  String number = "12";
  int intNumber = int.parse(number);
  double doubNumber = double.parse(number);
  //Numericos a String
  intNumber.toString(); //forma 1
  number = "$intNumber"; //forma 2
}



void operations(){
  int value1 = 12;
  int value2 = 3;
  value1 += value2; //sobreescribe value1; value1 = value1 + value2
  value1 -= value2;
  value1 *= value2;
  value1 ~/= value2; // ~/ division entera
  //Los strings son comparables por medio de == o !=
  String one, two;
  one = "Hola";
  two = "Chao";
  one == two; //false
  /*
  Las operaciones logicas disponibles en Dart son
  || ò
  && y
  ! desigual
  ?: operador ternario 
  */
}



void conditionals(){
  int num = 12;
  //Estructura if
  if (num != 12){

  } else if (num == 12){

  } else {

  }

  //Estructura Switch
  switch(num){
    case 1: break;
    case 2: break;
    default : print("else");
  }
}



void loops(){
  /*
  While: Ejecuta siempre y cuando la expresion sea verdadera
  */   
  while (true){
    break; 
  }
  /*
  do-while: Se ejecuta primero el codigo y luego se comprueba la condicion
  */
  do {
    int i = 12;
  } while (false);
  /*
  for
  */
  for(int i = 0; i < 10; i++){

  }

  Time time = Time.Soleado;
}



/*
Para dart las enumeraciones son nuevos tipos de datos
Las enumeraciones limitan las opciones que puede tener un tipo de dato. 
*/ 
enum Time {Soleado, LLuvioso, Despejado}



void colections(){
  List<String> names = ["Santiago","Nathalia", "Johana", "Sebastian", "Juana"];
  names.isEmpty; //false si no esta vacia
  names.isNotEmpty; //true si no esta vacia
  names.length; //numero de elementos de la lista
  names.add("David"); //agregar elemento a la lista
  names.remove("Santiago"); //quitar un elemento de la lista
  names.insert(2, "Santiago"); //agregar un elemento en un indice de la lista
  names.clear(); //borrar todos los elementos de la lista
  /*
  Set: No pueden tener valores duplicados
  El set no tiene insert en una posicion especifica, siempre agrega al final
  */
  Set<String> countries = {"Colombia", "Argentina", "Cuba", "Venezuela"};
  countries.add("Mexico"); //agregar elemento al final
  countries.elementAt(2); //obtener un elemento de un indice
  /*
  Map: Llave valor; diccionario.
  Por defecto tienen tipos de datos dinamicos
  */
  Map lastNames = {};
  Map<String, int> phones = {
    "Joha" : 123,
    "Santi" : 456,
  };
  phones.keys; //ver las llaves del diccionario
  phones.values; //ver los valores del diccionario
  phones.addAll({"David":312}); //añadir elemento a diccionario
  /*
  Uniendo colecciones
  */
  names.addAll(countries);
  Map phones2 = {
    ...phones //agrego todos los valores del diccionario phones al dict phones2
  };
  /*
  Podemos usar operadores condicionales en la declaracion de una coleccion
  */
  bool agregarAmarillo = true;
  List colores = [
    "rojo",
    "verde",
    if(agregarAmarillo == true) "amarillo",
  ];
  /*
  Podemos usar bucles en la declaracion de una coleccion
  */
  List coloresSecund = [
    "morado",
    "verde",
    for (int i = 0; i < colores.length; i++) colores[i] 
  ];
}



void main(){
  colections();
}
