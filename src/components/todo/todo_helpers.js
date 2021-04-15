export function reducer(state, action){
    switch(action.type){
        default:
            return {...state}
        case "COMPLETED":
            return {...state, }
        case "FETCH":
            return {...state,isLoading:false,isFetching:false,todos:action.payload}
    }
}
export const initialState = {
    todos:[],
    isLoading:true,
    due:0,
    isFetching:true,
    isOpen:false
}