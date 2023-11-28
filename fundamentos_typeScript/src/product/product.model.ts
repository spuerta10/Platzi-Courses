// archivo que guarda el modelado de los datos y definiciones de tipos

/*La palabra clave export sirve para poder importar los tipos de datos desde otro archivo*/
export type Sizes = "S" | "M" | "L" | "XL"; //creando una enumeracion
export type User = string | number //creo mi propio tipo de dato, 'literal type'
export type Product = {
    title:string,
    createdAt:Date,
    stock:number,
    size?:Sizes
}