import React, { useState } from "react";
import { useHistory } from "react-router-dom";

import Template from "../components/Template";
import { API_URL, TOKEN_SERIALIZER } from "../constants";

const CreateMenu = () => {
  const [menu, setMenu] = useState({
    description: "",
    name: "",
    start_date: "",
  });

  const history = useHistory();

  const handleChange = (e) => {
    setMenu((form) => ({
      ...form,
      [e.target.name]: e.target.value,
    }));
  };

  const handleCreate = async (e) => {
    e.preventDefault();
    console.log(menu.start_date);
    let dateSent = new Date(menu.start_date).getDate() + 1;
    let currentDay = new Date().getDate();

    if (dateSent < currentDay) {
      return window.alert("La fecha no puede ser menor a la actual");
    }

    const menuData = Object.assign({}, menu);

    menuData.description === "" &&
      Object.assign(menuData, { description: null });

    try {
      const create = await fetch(`${API_URL}/menu/`, {
        body: JSON.stringify(menu),
        method: "POST",
        headers: {
          Authorization: `token ${localStorage.getItem(TOKEN_SERIALIZER)}`,
          "Content-Type": "application/json",
        },
      });

      const { data } = await create.json();

      history.push(`/detail/${data.id}`);
    } catch (err) {
      console.log("err", err);
    }
  };

  return (
    <Template>
      <hr />
      <br />
      <button className="btn btn-info btn-md" onClick={() => history.goBack()}>
        Volver
      </button>
      <br />
      <br />
      <h1>Crear Menú Cornershop</h1>
      <br />
      <div className="row">
        <div className="col-md-5">
          <form className="form-group">
            <input
              className="form-control"
              type="text"
              onChange={handleChange}
              name="name"
              placeholder="Nombre del menú.."
              value={menu.name}
            />
            <br />
            <input
              className="form-control"
              type="text"
              onChange={handleChange}
              name="description"
              placeholder="Descripción del menú.."
              value={menu.description}
            />
            <br />
            <input
              className="form-control"
              type="date"
              onChange={handleChange}
              name="start_date"
              value={menu.start_date}
            />
            <br />
            <button
              type="submit"
              className="btn btn-success btn-block"
              onClick={handleCreate}
            >
              Crear Menú
            </button>
          </form>
        </div>
      </div>
    </Template>
  );
};

export default CreateMenu;
