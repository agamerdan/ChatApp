const roomName=JSON.parse(document.getElementById("room-name").textContent)
const user=JSON.parse(document.getElementById("user").textContent)
const inputItem=document.getElementById("comment")
const sendBtn=document.getElementById("send")
const messageArea=document.getElementById("conversation")



const chatSocket= new WebSocket('ws://'+ window.location.host+'/ws/chat/'+ roomName+ '/')

chatSocket.onmessage=function(e){
    const data=JSON.parse(e.data)
    var message_type=data.what_is_it
    if (message_type==="text") {
      var message=data.message
    }
    else if(message_type=="image"){
      var message=`<img src="${data.message}" width="200" hight="180">`
    }
    else if(message_type=="image"){
      var message=`<img src="${data.message}" width="200" hight="180">`
    }
    else if(message_type=="video"){
      var message=`<video width="320" height="240" controls><source src="${data.message}" ></video>`
    }
    else if(message_type=="audio"){
      var message=`<audio controls><source src="${data.message}" ></audio>`
    }
    
    if(user===data.user){
      messageArea.innerHTML+=`<div class="row message-body">
    <div class="col-sm-12 message-main-sender">
      <div class="sender">
        <div class="message-text">
         ${message}
        </div>
        <span class="message-time pull-right">
        ${data.created_date}
        </span>
      </div>
    </div>
  </div>`
    }
    else{
      messageArea.innerHTML+=`<div class="row message-body">
    <div class="col-sm-12 message-main-receiver">
      <div class="receiver">
        <div class="message-text">
         ${message}
        </div>
        <span class="message-time pull-right">
         ${data.created_date}
        </span>
      </div>
    </div>
  </div>`

    }
    

}


const file=document.getElementById("file").addEventListener('change', handleFileSecect, false)

function handleFileSecect(){
 var resim=document.getElementById("file").files[0]
 getBase64(resim)
}

function getBase64(resim){
  var reader= new FileReader()
  reader.readAsDataURL(resim)
  var type=resim.type.split("/")[0]
 

  reader.onload=function(){
    chatSocket.send(JSON.stringify({
      "what_is_it":type,
      "message":reader.result,
    }))
  }
}

chatSocket.onclose=function(e){
    console.error("Baglantı kesildi")
}

inputItem.focus()

inputItem.onkeyup=function(e){
    if(e.keyCode===13){
        sendBtn.click();
    }
 
}

sendBtn.onclick=function(e){
    const message=inputItem.value
    chatSocket.send(JSON.stringify({
        "what_is_it":"text",
        "message":message
    }))
    inputItem.value=" "
}