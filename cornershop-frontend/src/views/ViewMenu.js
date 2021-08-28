import React, { useEffect, useState } from "react";
import { useParams, useHistory } from "react-router-dom";

import { API_URL, TOKEN_SERIALIZER } from "../constants";

import Template from "../components/Template";

import useDispatcher from "../hooks/useDispatcher";

const ViewMenu = () => {
  const [menu, setMenu] = useState(null);

  const [access, setAccess] = useState(null);

  const [form, setForm] = useState({
    username: "",
    password: "",
  });

  const [option, setOption] = useState("");

  const [customization, setCustomization] = useState("");

  const dispatcher = useDispatcher();

  const { uuid } = useParams();

  useEffect(() => {
    const fetchDetailMenu = async () => {
      try {
        const detail = await fetch(`${API_URL}/menu/${uuid}`, {
          headers: {
            Authorization: `token ${localStorage.getItem(TOKEN_SERIALIZER)}`,
          },
        });

        const { data } = await detail.json();

        setMenu(data);

        if (data.menu.options.length > 0) {
          setOption(data.menu.options[0].description);
        }
      } catch (e) {
        console.log("err", e);
      }
    };

    fetchDetailMenu();
  }, [uuid, access]);

  const handleChange = (e) => {
    setForm((state) => ({
      ...state,
      [e.target.name]: e.target.value,
    }));
  };

  const handleLogin = async (e) => {
    e.preventDefault();

    try {
      const login = await fetch(`${API_URL}/accounts/signin/`, {
        body: JSON.stringify(form),
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
      });

      const user = await login.json();

      if (user.code == 200){
        localStorage.setItem(TOKEN_SERIALIZER, user.data.token);

      setAccess(true);

      dispatcher((dispatch) => ({
        ...dispatch,
        user: user.data,
      }));
      }else{
        return window.alert(user.errors);
      }
    } catch (e) {
      console.log("err", e);
    }
  };

  const handleCreateOrder = async (e) => {
    e.preventDefault();


    try { 
      const { id } = menu.options.find(menuOption => menuOption.description === option);

      const order = await fetch(`${API_URL}/order/`, {
        body: JSON.stringify({
          optionId: id,
          customization
        }),
        method: 'POST',
        headers: {
          'Authorization': `token ${localStorage.getItem(TOKEN_SERIALIZER)}`,
          'Content-Type': 'application/json'
        }
      });

      const { message, data } = await order.json();

      if (message === "ValueError") {
        return window.alert('No se puede crear la orden después de las 11 AM');
      }
      window.alert(`La orden ha sido creada con éxito, N. Orden ${data.id}`);

      window.localStorage.clear();

      window.location.href = "/";
    } catch (err) {
      console.log('e', err);
    }
  }

  return (
    <Template>
      <div>
        {menu && access ? (
          <>
            <hr />
            <h1>Menu del día</h1>
            <p>{menu.name}</p>
            <br />
            <div className="row">
              <div className="col-md-8">
                <table className="table text-center">
                  <thead>
                    <tr>
                      <th scope="col">Opción</th>
                      <th scope="col">Descripción</th>
                    </tr>
                  </thead>
                  <tbody>
                    {menu.options.map((option) => (
                      <tr key={option.id}>
                        <th scope="row">{option.id}</th>
                        <th>{option.description}</th>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
              <div className="col-md-4">
                <form onSubmit={handleCreateOrder}>
                  <div className="form-group">
                    <label className="h6">Escoge una orden</label>
                    <select
                      onChange={(e) => setOption(e.target.value)}
                      className="form-control"
                      value={option}
                    >
                      {menu.options.map((option) => (
                        <option key={option.id}>{option.description}</option>
                      ))}
                    </select>
                  </div>
                  <div className="form-group">
                    <input
                      className="form-control"
                      type="text"
                      name="customization"
                      onChange={(e) => setCustomization(e.target.value)}
                      value={customization}
                      placeholder="Personalizar"
                    />
                  </div>
                  <div className="form-group">
                    <button type="submit" className="btn btn-primary">
                      Crear Orden
                    </button>
                  </div>
                </form>
              </div>
            </div>
          </>
        ) : (
          <>
            <div className="row">
              <div className="col-md-4">
                <form className="form-group" onSubmit={handleLogin}>
                  <input
                    className="form-control"
                    name="username"
                    onChange={handleChange}
                    value={form.username}
                    type="text"
                    placeholder="Username..."
                  />
                  <br />
                  <input
                    className="form-control"
                    name="password"
                    onChange={handleChange}
                    value={form.password}
                    type="password"
                    placeholder="Password..."
                  />
                  <br />
                  <button
                    className="btn btn-sm bg-primary text-white"
                    type="submit"
                  >
                    Login
                  </button>
                </form>
              </div>
            </div>
          </>
        )}
      </div>
    </Template>
  );
};

export default ViewMenu;
