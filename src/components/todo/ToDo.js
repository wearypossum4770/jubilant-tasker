import { useEffect , useReducer} from "react"
import {reducer, initialState} from './todo_helpers'
export default function ToDo(){
    const [state, dispatch] = useReducer(reducer, initialState)
    useEffect(()=>{
        try{
            let url = "http://127.0.0.1:8000/tasks/"
            let options = {mode:"cors", headers:{"Content-Type": "application/json"}}        
            async function fetchData(){
            const request =  await ( await fetch(url, options)).json()
                    dispatch({type:"FETCH", payload:request})
            }
            fetchData()
    }catch(error){
        console.log(error)
    }
},[])
let {todos,isLoading} = state
let instance = {
    
    overdue:0, 
    completed(){return this.todos.filter(todo=>todo.completed).lenth}, 
    total(){return this.todos.length},not_completed:0,
}

console.log(todos[0])
console.log(state)
return (
    <div>
 <div>
 <label htmlFor="new_todo"> New Todo
            <input name="new_todo"/>
        </label>
 </div>
    {isLoading?<div>Loading...</div>:<div>{todos.map((todo,index)=><div><label htmlFor={index}><input type="checkbox"/>{`${todo.title} - ${todo.content}`}</label></div>)}</div>}
    </div>
)

}
/**Telemetry
---------
The .NET tools collect usage data in order to help us improve your experience. It is collected by Microsoft and shared with the community. You can opt-out of telemetry by setting the DOTNET_CLI_TELEMETRY_OPTOUT environment variable to '1' or 'true' using your favorite shell.

Read more about .NET CLI Tools telemetry: https://aka.ms/dotnet-cli-telemetry

Configuring...
--------------
A command is running to populate your local package cache to improve restore speed and enable offline access. This command takes up to one minute to complete and only runs once.
Processing triggers for man-db (2.9.1-1) ... */