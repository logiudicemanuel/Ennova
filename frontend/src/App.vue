<template>
  <div id="app">
    <!--Div contenente l'home-page, dove è possibile aggiungere - modificare - eliminare elementi-->
    <div v-if="isVisible">
      <img class="elmec" src="./img/elmec_white.png">
      <img class="fendi" src="./img/fendi.png">
      <br>
      <div class="titolo">
        <h1>Riparazione Ennova</h1>  
      </div>
      <button class="buttonRicerca" @click="toggleDiv">Ricerca Telefono</button>
      <br>
      <br>
      <p>Oppure</p>
      <h3>Inserisci Nuovo Telefono : </h3>
      <form @submit.prevent="submitForm"><!--Form per l'inserimento dei dati-->
        <div class="row">
          <input v-model="element.ticket" type="text" class="ins" placeholder="Ticket">
          <input v-model="element.seriale" type="text" class="ins" placeholder="Seriale">
          <input v-model="element.imei" type="text" class="ins" placeholder="Imei">
          <input v-model="element.stato" type="text" class="ins" placeholder="Stato">
          <input v-model="element.tipo_guasto" type="text" class="ins" placeholder="Tipologia Guasto">
          <button id="inviaIns">Invia</button>
        </div>
      </form>
      <hr>
      <p>Fai doppio click su un qualsiasi elemento per modificarlo!</p>
      <table><!--Tabella contenente tutti gli elementi del db-->
        <thead class="titoloTabella">
          <th>Ticket<a class="hda" href="https://hda.elmec.ad/HDAPortal/#/Page/Home" target="_blank">?</a></th><!-- Il ? Apre HelpDesk Advanced, per ricercare i vari ticket-->
          <th>Seriale</th>
          <th>Imei</th>
          <th>Stato</th>
          <th>Tipo Guasto</th>
          <th>Canc</th>
        </thead>
        <tbody class="corpoTabella">  
          <!--ciclo for per replicare il tbody n volte relativamente al numero di elementi presenti nel db-->
          <!--facendo un doppio click su un qualsiasi elemento è possibile procedere con la modifica di esso-->
          <tr v-for="elementi in lista" :key="elementi.id" @dblclick="$data.element = elementi">
            <td>{{ elementi.ticket }}</td>
            <td>{{ elementi.seriale }}</td>
            <td>{{ elementi.imei }}</td>
            <td>{{ elementi.stato }}</td>
            <td>{{ elementi.tipo_guasto }}</td>
            <td>
              <button id="canc" @click="deleteElement(elementi)">X</button><!--cancella l'elemento dal db richiamando il metodo deleteElement-->
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <!--Div contenente la parte di ricerca di un elemento, con la successiva possibilità di modificarlo o eliminarlo-->
    <div v-if="isVisible2">
      <img class="elmec" src="./img/elmec_white.png">
      <img class="fendi" src="./img/fendi.png">
      <br>
      <div class="titolo">
        <h1>Riparazione Ennova</h1>  
      </div>
      <button class="buttonRicerca" @click="toggleDiv">Inserisci Telefono</button>
      <br>
      <br>
      <h3>Inserisci Campi Di Ricerca : </h3>
      <form @submit.prevent="submitRicerca"><!--Form che permette l'inserimento del campo da ricercare poi tramite il metodo submitRicerca-->
       <div class="row">
          <input v-model="ricerca.campo" type="text" class="ins-ricerca" placeholder="Campo">
          <button id="inviaRic">Ricerca</button>
       </div>
      </form>
      <hr>
      <p>Modifica i campi selezionati : </p>
      <form @submit.prevent="submitFormRicerca"><!--Form che verrà utilizzato per la modifica dei dati, dopo aver fatto doppio click su un qualsiasi elemento della tabella-->
        <div class="row">
          <input v-model="element.ticket" type="text" class="ins" placeholder="Ticket">
          <input v-model="element.seriale" type="text" class="ins" placeholder="Seriale">
          <input v-model="element.imei" type="text" class="ins" placeholder="Imei">
          <input v-model="element.stato" type="text" class="ins" placeholder="Stato">
          <input v-model="element.tipo_guasto" type="text" class="ins" placeholder="Tipologia Guasto">
          <button id="inviaIns">Modifica</button>
        </div>
      </form>
      <hr>
      <p>Fai doppio click su un qualsiasi elemento dopo la ricerca per modificarlo!</p>
      <table><!--Tabella contenente tutti gli elementi del db relativi a ciò che è stato inserito nel form di ricerca-->
        <thead class="titoloTabella">
          <th>Ticket<a class="hda" href="https://hda.elmec.ad/HDAPortal/#/Page/Home" target="_blank">?</a></th><!-- Il ? Apre HelpDesk Advanced, per ricercare i vari ticket-->
          <th>Seriale</th>
          <th>Imei</th>
          <th>Stato</th>
          <th>Tipo Guasto</th>
          <th>Canc</th>
        </thead>
        <tbody class="corpoTabella">
          <!--ciclo for per replicare il tbody n volte relativamente al contenuto della lista caricata con SOLAMENTE gli elementi -->
          <!--facendo un doppio click su un qualsiasi elemento è possibile procedere con la modifica di esso-->
          <tr v-for="elementi in listaRicerca" :key="elementi.id" @dblclick="$data.element = elementi">
            <td>{{ elementi.ticket }}</td>
            <td>{{ elementi.seriale }}</td>
            <td>{{ elementi.imei }}</td>
            <td>{{ elementi.stato }}</td>
            <td>{{ elementi.tipo_guasto }}</td>
            <td>
              <button id="canc" @click="deleteElement(elementi)">X</button><!--cancella l'elemento dal db richiamando il metodo deleteElement-->
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<!--VUE JS-->
<script>
export default{
  name: 'App',
  data(){
    return{
      element:{
        'ticket': '',
        'seriale':'',
        'imei': '',
        'stato': '',
        'tipo_guasto': '',
      
      },
      lista: [],
      listaRicerca: [],
      isVisible : true,
      isVisible2 : false,
      ricerca:{
      'campo': '',
      }
    }
},
async created(){
  await this.getLista();
},
methods:{
  submitForm(){//verifica se l'elemento che si è andato a inserire è già presente o meno, in base a ciò lo modifica o ne inserisce uno nuovo
    if(this.element.id === undefined){
      this.createElement();
    }else{
      this.editElement();
    }
  },
  submitFormRicerca(){//permette solo la modifica del elemento selezionato
    this.editElement();
  },
  async getLista(){//carica la lista con gli elementi del db
    var risposta = await fetch('http://127.0.0.1:8000/api/todo/');
    this.lista = await risposta.json();
  },
  async createElement(){//permette la creazione di un nuovo elemento nel db
    await this.getLista();
    await fetch('http://127.0.0.1:8000/api/todo/', {
      method:'post',
      headers:{
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(this.element)
    });
    await this.getLista();
      this.element={};
    },
    async editElement(){//permette la modifica di un nuovo elemento nel db
      await this.getLista();
      await fetch(`http://127.0.0.1:8000/api/todo/${this.element.id}/`, {
        method:'put',
        headers:{
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.element)
      });
      await this.getLista();
      this.element = {};
    },
    async deleteElement(element){//permette l'eliminazione di un nuovo elemento nel db
      await this.getLista();
      await fetch(`http://127.0.0.1:8000/api/todo/${element.id}/`, {
        method:'delete',
        headers:{
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.element)
      });
      await this.getLista();
      this.submitRicerca();
      this.submitRefresh();
      this.element = {};
        
    },
    toggleDiv(){//gestisce quale div (se quello della ricerca o del homepage) visualizzare
      this.isVisible=!this.isVisible;
      this.isVisible2=!this.isVisible2;
    },
    async submitRicerca(){//permette la ricerca di un elemento nel db
      this.listaRicerca= [];
      await this.getLista();
      var x = 0;
      for(var i = 0; i<this.lista.length;i++){
        if(this.ricerca.campo === this.lista[i].ticket || this.ricerca.campo === this.lista[i].seriale || this.ricerca.campo === this.lista[i].imei || this.ricerca.campo === this.lista[i].stato || this.ricerca.campo === this.lista[i].tipo_guasto || this.ricerca.campo === this.lista[i].note){
          this.listaRicerca[x] = this.lista[i];
          x++;
        }
      }
      if(x === 0){
        this.listaRicerca= [];
      }
    },
    submitRefresh(){//riduce la lunghezza della listaRicerca dopo l'eliminazione di un elemento
      this.listaRicerca.length=this.listaRicerca.length-1;
    },
  }
}
</script>

<!--CSS-->
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 25px;
}
#login {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 25px;
}
#logout{
  float: right;
}
#Login{
  float: left;
}
.ins{
  width: 18%;
  margin:auto;
  font-size: 90%;
  border-radius: 5px;
  border: grey solid 1px;
  background-color: white;
}
.ins-ricerca{
  width: 65%;
  margin:auto;
  margin-bottom: 1%;
  text-align: center;
}
.buttonRicerca{
  margin: auto;
  width: 18%;
  background-color: #13a837;
  border: seagreen solid 1px;
  border-radius: 5px;
  color: white;
}
#inviaIns{
  margin: auto;
  width: 8%;
  background-color: #13a837;
  border: seagreen solid 1px;
  border-radius: 5px;
  color: white;
}
#inviaRic{
  margin: auto;
  width: 65%;
  background-color: #13a837;
  border: seagreen solid 1px;
  border-radius: 5px;
  color: white;
}
table{
  width: 90%;
  margin: auto;
}
#canc{
  color: red;
  font-size: 80%;
  border: 1px solid red;
  border-radius: 5px;
  background-color: white;
}
.corpoTabella{ 
  height: 100%;
}
.corpoTabella tr{ 
  height: 40px;
  border-bottom: #d3d3d3 solid 1px;
}
.corpoTabella td{ 
  border-right: #d3d3d3 solid 1px;
  border-left: #d3d3d3 solid 1px;
}
.titoloTabella{
  height: 100%;
  border: #2c3e50 solid 1px;
}
.titoloTabella th{
  height: 100%;
  border-right: #2c3e50 solid 1px;
}
.fendi{
  width: 10%;
  height: 10%;
  float: right;
}
.elmec{
  width: 20%;
  height: 20%;
  float: left;
}
.collab{
  float: left;  
  margin-left:1%;
}
.titolo{
  margin-top: 5%;
}
.hda{
  border: solid #ffa500 2px;
  border-radius: 10px;
  color: #ffa500 ;
  margin-left: 5%;
  
}
@media only screen and (max-width: 1000px){
  .ins{
    width: 65%;
    margin:auto;
    margin-bottom: 1% ;
  }
  .ins-ricerca{
    width: 65%;
    margin: auto;
    margin-bottom: 1% ;
  }
  #inviaIns{
    margin: auto;
    width: 65%;
    height: 65%;
  }
  #inviaRic{
    margin: auto;
    width: 65%;
    height: 65%;
  }
  .corpoTabella{ 
    font-size: 78%;
  }
  .titoloTabella{
    font-size: 78%;
  }
  table{
    width: 20%;
    margin: auto;
  }
  #canc{
    font-size: 100%;
    border: solid red 1px;
    background-color: white;
  }
  .fendi{
  width: 10%;
  height: 10%;
  float: right;
  }
  .elmec{
    width: 20%;
    height: 20%;
    float: left;
  }
  .collab{
    float: left;  
    margin-left:1%;
  }
  .buttonRicerca{
  margin: auto;
  width: 25%;
}
}
</style>