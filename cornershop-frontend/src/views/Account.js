import React, { useEffect, useState } from "react";
import { useHistory } from "react-router-dom";

import Template from "../components/Template";

import { API_URL, TOKEN_SERIALIZER } from "../constants";
import useAuth from "../hooks/useAuth";

const Account = () => {
  const [menu, setMenu] = useState([]);

  const [orders, setOrders] = useState([]);

  const { user } = useAuth();

  const history = useHistory();

  useEffect(() => {
    const fetchMenus = async () => {
      const getMenus = await fetch(`${API_URL}/menu/`, {
        headers: {
          Authorization: `token ${localStorage.getItem(TOKEN_SERIALIZER)}`,
        },
      });

      console.log("getMenus", getMenus);

      const menus = await getMenus.json();

      console.log("menus", menus);

      setMenu(menus.results);
    };

    fetchMenus();
  }, []);

  const handleCreateMenu = () => {
    history.push("/create/menu");
  };

  return (
    <Template>
      <hr />
      <br />
      <div className="row">
        <div className="col-md-4">
          <h4>Menu Cornershop</h4>
          <br />
          <button className="btn btn-info btn-md" onClick={handleCreateMenu}>
            Crear Menu
          </button>
          <br />
          <br />
          <button
            className="btn btn-dark btn-md"
            onClick={() => history.push("/orders")}
          >
            Listar Ordenes
          </button>
        </div>
        <div className="col-md-8">
          {menu.length === 0 ? (
            <h4>No hay registros disponibles</h4>
          ) : (
            <table className="table table-stripped text-center">
              <thead>
                <tr>
                  <th scope="col">#</th>
                  <th scope="col">Día</th>
                  <th scope="col">Nombre</th>
                  <th scope="col">Autor</th>
                  <th scope="col">Opciones</th>
                  <th scope="col">Acciones</th>
                </tr>
              </thead>
              <tbody>
                {menu.map((item) => (
                  <tr key={item.id}>
                    <th scope="row">{item.id}</th>
                    <td>{item.start_date}</td>
                    <td>{item.name}</td>
                    <td>{user && user.username}</td>
                    <td>{item.options && item.options.length}</td>
                    <td className="d-flex justify-content-around">
                      <button
                        className="btn btn-primary btn-sm"
                        onClick={() => history.push(`/edit/detail/${item.id}`)}
                      >
                        E
                      </button>
                      <button
                        className="btn btn-success btn-sm"
                        onClick={() => history.push(`/detail/${item.id}`)}
                      >
                        V
                      </button>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          )}
        </div>
      </div>
    </Template>
  );
};

export default Account;
