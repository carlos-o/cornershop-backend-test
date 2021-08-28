import React, { useEffect, useState } from 'react';
import Template from '../components/Template';
import { API_URL, TOKEN_SERIALIZER } from '../constants';
import { useHistory } from 'react-router-dom';

const Orders = () => {
  const [orders, setOrders] = useState([]);

  const history = useHistory();

  useEffect(() => {
    const handleGetOrders = async () => {
      try {
        const req = await fetch(`${API_URL}/order`, {
          headers: {
            'Authorization': `token ${localStorage.getItem(TOKEN_SERIALIZER)}`
          }
        })
  
        const { results } = await req.json();
  
        setOrders(results);
      } catch (err) {
        console.log('err', err);
      }
    }

    handleGetOrders();
  }, []);

  return (
    <Template>
      <hr />
      <button className="btn btn-info btn-md" onClick={() => history.goBack()}>
        Volver
      </button>
      <br />
      <br />
      <table className="table">
        <thead>
          <tr>
            <th scope="col">Fecha</th>
            <th scope="col">Orden</th>
            <th scope="col">Rut</th>
            <th scope="col">Nombre</th>
            <th scope="col">Menu</th>
            <th scope="col">Opcion</th>
            <th scope="col">Accion</th>
          </tr>
        </thead>
        <tbody>
          {orders.map(order => (
            <tr key={order.id}>
              <th scope="row">{order.created_at}</th>
              <th>{order.id}</th>
              <th>{order.rut}</th>
              <th>{order.name}</th>
              <th>{order.menu}</th>
              <th>{order.option}</th>
              <th>
                <button className="btn btn-sm btn-primary" onClick={() => window.alert(order.customization)}>
                  V
                </button>
              </th>
            </tr>
          ))}
        </tbody>
      </table>
    </Template>
  )
}

export default Orders;