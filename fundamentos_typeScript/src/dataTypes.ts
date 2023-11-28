(() => {
    let age:number /*type annotation*/ = 12;
    let flag: boolean = true;
    const productStock = 1000;
    let nan:number = NaN; //NaN tambien es de tipo number
    let greaterThan:string = Math.random() >= 0.5 ? 'true' : 'false'; //condicionales de una linea
    let message:string = `El numero es mayor que 0.5 ${greaterThan}` //creacion de multiline String con el uso de backticks
    let array: (number | boolean | string)[] = ["Hola"]; //array que permite number, string, boolean
    let productPrice:number = 12;
    let anotherProduct:string = "12";
    let myVar: any; //cualquier tipo de dato, no deberia de ser usado
    myVar as string; //tipar una var tipo any
    let myName: (string | number) = "Hola"; //union type para permitir diferentes tipos de datos

    type user = string | number //creo mi propio tipo de dato, 'literal type'
    type shirtSize = "S" | "M" | "L" | "XL" //creando una enumeracion
    
    function sayHi(name:string | null){
        let hello = "Hi ";
        //pregunto si el dato no es nulo para pasar el nombre a lower case, en caso contrario pongo nobody
        hello += name?.toLowerCase() || "nobody";
        console.log(hello);
    }

    const sumValues = (value1:number, value2:number):number => { /*tambien hay funciones void (no retornan nada)*/
        return value1 + value2
    }

    const product2Json = ( /*Ejemplo de una arrow function*/
        title:string,
        creationDate:Date,
        stock?:number  //el signo de pregunta es para declarar que el campo es opcional/ 
    ) => ({
        title,
        creationDate,
        stock
    }) //retorno explicito


    type User = {
        email:string,
        password:string
    } //objeto diccionario

    const login = (
        user:User
    ) => {console.log(user.email, user.password)}

})(); 
/*
funcion anonima autoejecutada para que el 
scope de las variables no me afecte otros programas.
*/
