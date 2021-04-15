import {useEffect} from 'react'
export default function FetchData({url=""}){
    let options = {mode:"cors", headers:{"Content-Type": "application/json"}}
    let resp=[]
useEffect(()=>{
    try{
        async function fetchData(){
            const request =  await ( await fetch(url, options)).json()
            resp.push(request)
            }
            fetchData()
    }catch(error){
        console.log(error)
    }
})
        return resp
}