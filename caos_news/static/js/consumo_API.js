//Obtener y mostrar juegos destacados
async function  obtenerJuegos(){
    //Configurar las opciones del fetch
    const options = {
        method: 'GET',
        headers: {
            'X-RapidAPI-Key': '969b29bd8fmsh11d54b0c9451712p16fc47jsn459bc844da4c',
            'X-RapidAPI-Host': 'epic-store-games.p.rapidapi.com'
        }
        };
        
    //Parametros requeridos por API
    const searchWords = 'Mount';
    const locale = 'cl';
    const country = 'cl';  
    const url = `https://epic-store-games.p.rapidapi.com/onSale?searchWords=${searchWords}&locale=${locale}&country=${country}`;
    

    let response = await fetch(url, options)
    const data = await response.json() //Parsea la respuesta del fetch a JSON
    return data 
}

function crearCard(juegos){
    let lista = [] //Declaración de arreglo donde se guardarán las cards creadas

    // Creación de cards
    for (let index = 0; index < 5; index++) {
        //Obtener información relevante de la lista "juegos"
        let precio =  juegos[index].currentPrice/100
        let titulo =  juegos[index].title
        let imagen =  juegos[index].keyImages[0].url
        let publisher =  juegos[index].publisherName
        let url = juegos[index].url

        let card = `<div class="card mb-3 bg-dark"  >
                        <div class="row g-0">
                            <div class="col-md-4 bg-dark">
                                <img src=${imagen} class="img-fluid rounded-start" alt="...">
                            </div>
                            <div class="col-md-8 text-light bg-dark">
                                <div class="card-body">
                                    <h5 class="card-title">${titulo}</h5>
                                    <p>Publisher: ${publisher}</p>
                                    <p>Precio: CLP ${precio}</p>
                                    <a href=${url} class="btn btn-light mt-auto" target="blank">Ir a Epic Store</a>
                                </div>
                            </div>
                        </div>
                    </div>`
        lista.push(card) //Almacenar la card creada en la lista  
    }
    return lista
}

let juegos; 

(async () =>{
     juegos = await obtenerJuegos() 
     let arreglo = crearCard(await juegos)
     $(document).ready(function(){ //se ejecutará cuando el documento esté cargado
        arreglo.forEach(element => {
            $("#juegos-destacados").append(element) //Agregar las cards al contenedor 
         });
    })
})(); //Funcion asincrona autoejecutable