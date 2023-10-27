import {useEffect} from 'react'
import {getAllClients} from '../api/client.api'


export function ItemList() {

useEffect(() => {
    
    async function loadClients(){
        const res = await getAllClients();
        console.log(res);
    } 
    loadClients();
}, [])
    return <div>ItemList</div>;
}