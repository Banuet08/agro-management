import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'
import { ShippingPage } from './ShippingPage'
import { ClientFormPage } from './ClientFormPage'
import { ProductFormPage } from './ProductFormPage'
import { DriverFormPage } from './DriverFormPage'
import { TruckFormPage } from './TruckFormPage'
import { ContainerFormPage } from './ContainerFormPage'
import { CustomFormPage } from './CustomFormPage'
import { Navigation } from '../components/Navigation'

export function MainPage() {
  return (
    <BrowserRouter>

      <Navigation/>

      <Routes>
        <Route path="/shipping" element={<ShippingPage />} />
        <Route path="/client-create" element={<ClientFormPage />} />
        <Route path="/product-create" element={<ProductFormPage />} />
        <Route path="/driver-create" element={<DriverFormPage />} />
        <Route path="/truck-create" element={<TruckFormPage />} />
        <Route path="/container-create" element={<ContainerFormPage />} />
        <Route path="/custom-create" element={<CustomFormPage />} />

      </Routes>
    </BrowserRouter>
  )
}

export default MainPage