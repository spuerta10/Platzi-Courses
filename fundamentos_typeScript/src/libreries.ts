//npm install nombre-libreria
import {subDays, format} from 'date-fns';

const date = new Date(2016, 1, 1);
const rta = subDays(date, 20); //restar 20 dias a la fecha

//librerias no adaptadas para TS
import _ from 'lodash';

const data = [
    {
        username : 'nico',
        role : 'admin'
    },
    {
        username : 'valentina',
        role : 'vendor'
    },
    {
        username : 'santiago',
        role : 'customer'
    },
    {
        username : 'andres',
        role : 'admin'
    },
];

_.groupBy(data, (item) => item.role); 