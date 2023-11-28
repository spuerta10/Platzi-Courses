/*
Ejecutar en terminal:
npx tsc ruta --target es6 -> para transpilar codigo TS a
                               una version definida de ecmascript
npx tsc ruta --target es6 --outDir dist -> outDir para mandar archivos transpilados
                                           a la carpeta dist
npx tsc --watch -> Para que se transpile automaticamente los archivos al
                   detectar un cambio en los mismos.
*/

let myName = "Santiago";
console.log(myName);