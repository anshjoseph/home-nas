const upload_form = document.getElementById("upload-form")
const submit_btn = document.getElementById("submit-btn")
// 
// 
const user = document.getElementById("user")
const title = document.getElementById("title")
const file = document.getElementById('file')
const datatype = document.getElementById('datatype')
const decs = document.getElementById('decs')
// 
// 
const progress_box = document.getElementById('progress_box')
const cancle_box = document.getElementById('cancal_box')
const cancle_btn = document.getElementById('cancle-btn')
// 
// 
const csrf = document.getElementsByName('csrfmiddlewaretoken')


submit_btn.addEventListener('click',()=>{
    
    const User = user.value
    const Title = title.value
    const Data = file.files[0]
    const Data_Type = datatype.value
    const Decs = decs.value
    
    

    if(User != undefined && Title != undefined && Data != undefined && Data_Type != undefined){
        // console.log(User,Title,Data,Data_Type);
        progress_box.classList.remove("not_vis")
        cancle_box.classList.remove("not_vis")
        const form_data = new FormData()
        form_data.append('csrfmiddlewaretoken',csrf[0].value)
        form_data.append('user',User)
        form_data.append('title',Title)
        form_data.append('file',Data)
        form_data.append('decs',Decs)
        form_data.append('data_type',Data_Type)
        $.ajax({
            type: "POST",
            url: upload_form.action,
            data: form_data,
            dataType: upload_form.enctype,
            beforeSend: function(){

            },
            xhr: function () { 
                const xhr = new window.XMLHttpRequest()
                xhr.upload.addEventListener('progress',e=>{
                    if(e.lengthComputable){
                        const per = e.loaded / e.total * 100
                        progress_box.innerHTML=`
                        <div class="progress">
                            <div  class="progress-bar" role="progressbar" style="width:${per}%" aria-valuenow="${per}" aria-valuemin="0" aria-valuemax="100"></div>
                        </div>
                        <br>
                        <p>${per.toFixed(1)}%</p>
                        `
                    }
                })
                cancle_btn.addEventListener('click', ()=>{
                    xhr.abort()
                    progress_box.classList.add("not_vis")
                    cancle_box.classList.add("not_vis")
                })
                return xhr
            },
            success: function (response) {
                console.log("s")
                // response.responseText
                if(response.responseText != undefined){
                    document.getElementById('hjeguygfguewtggdsfrg').innerHTML = response.responseText
                }
                
            },
            error: function(error){
                // document.getElementById('hjeguygfguewtggdsfrg').innerHTML = error.responseText
                console.log("e")
                if(error.responseText != undefined){
                    document.getElementById('hjeguygfguewtggdsfrg').innerHTML = error.responseText
                }
            },
            cache: false,
            contentType: false,
            processData: false,
        });
    }
    else{
        alert("pls fill all the feilds with valid data")
    }
    
})
// 
// 
// 
