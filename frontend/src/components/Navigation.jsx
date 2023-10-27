import {Link} from 'react-router-dom'

export function Navigation(){
    return (
    <div>
        <Link to="/main"><h1>Main Page</h1></Link>
        <Link to="/shipping"><h1>Shipping</h1></Link>
        <Link to="/client-create">create client</Link>
        <Link to="/product-create">create product</Link>
        <Link to="/driver-create">create driver</Link>
        <Link to="/truck-create">create truck</Link>
        <Link to="/container-create">create container</Link>
        <Link to="/custom-create">create custom</Link>
    </div>
    )
}