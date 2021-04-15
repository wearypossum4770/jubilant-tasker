import {useEffect} from 'react'
export default function usePostData(url="", data={}){
    let options = {method:"POST",mode:"cors",body:JSON.stringify(data), headers:{"Content-Type": "application/json"}}
    let resp=[]
useEffect(()=>{
    try{
        async function postData(){
            const request =  await ( await fetch(url, options)).json()
            resp.push(request)
            }
            postData()
    }catch(error){
        console.log(error)
    }
})
        return resp
}