import React, { useEffect, useState } from "react";
import { useParams, useHistory } from "react-router-dom";

import Template from "../components/Template";
import { API_URL, TOKEN_SERIALIZER } from "../constants";

const EditMenu = () => {
  const { id } = useParams();

  const [detail, setDetail] = useState(null);

  const history = useHistory();

  useEffect(() => {
    const fetchDetailMenu = async () => {
      try {
        const menu = await fetch(`${API_URL}/menu/${id}`, {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
            Authorization: `token ${localStorage.getItem(TOKEN_SERIALIZER)}`,
          },
        });

        const { data } = await menu.json();

        setDetail(data);
      } catch (e) {
        console.log("err", e);
      }
    };

    fetchDetailMenu();
  }, [id]);

  const handleClickCreateMenu = () => {
    history.push(`/create/option/${id}`);
  };

  const handleDeleteConfirmation = async (option) => {
    if (window.confirm("¿Está seguro que desea eliminar esta opción?")) {
      try {
        await fetch(`${API_URL}/menu/${id}/option/${option}`, {
          method: "DELETE",
          headers: {
            "Content-Type": "application/json",
            Authorization: `token ${localStorage.getItem(TOKEN_SERIALIZER)}`,
          },
        });

        setDetail((details) => ({
          ...details,
          options: details.options.filter(
            (currentOptionLocal) => currentOptionLocal.id !== option
          ),
        }));
      } catch (err) {
        console.log("err", err);
      }
    }
  };

  const handleSendSlackNotification = async () => {
    try {
      const remider = await fetch(`${API_URL}/menu/${id}/send-reminder/`, {
        headers: {
          "Content-Type": "application/json",
          Authorization: `token ${localStorage.getItem(TOKEN_SERIALIZER)}`,
        },
      });

      const { code } = await remider.json();

      if (code === 400) {
        return window.alert("Ya se envio la notificacion");
      } else {
        window.alert("La notificacion ha sido enviada con exito");
        history.push("/account");
      }
    } catch (err) {
      console.log("err", err);
    }
  };

  const handleClickListMenu = () => {
    history.push("/account");
  };

  return (
    <Template>
      <hr />
      <br />
      {detail && (
        <>
          <h1>{detail.name}</h1>
          <p>{detail.start_date}</p>
          <div className="row">
            <div className="col-md-6">
              <div className="d-flex justify-content-around">
                <button
                  className="btn btn-md bg-primary text-white"
                  onClick={handleClickCreateMenu}
                >
                  Agregar Opción al Menú
                </button>
                <button
                  className="btn btn-md bg-primary text-white"
                  onClick={handleClickListMenu}
                >
                  Listar Menú
                </button>
                {detail.options.length > 0 && (
                  <button
                    className="btn btn-md bg-success text-white"
                    onClick={handleSendSlackNotification}
                  >
                    Enviar Recordatorio
                  </button>
                )}
              </div>
              <br />
            </div>
            <div className="col-md-12">
              <table className="table text-center">
                <thead>
                  <tr>
                    <th scope="col">#</th>
                    <th scope="col">Descripción</th>
                    <th scope="col">Acciones</th>
                  </tr>
                </thead>
                <tbody>
                  {detail.options.map((option) => (
                    <tr key={option.id}>
                      <th scope="row">{option.id}</th>
                      <td>{option.description}</td>
                      <td className="d-flex justify-content-center">
                        <button
                          className="btn btn-primary btn-sm mr-5"
                          onClick={() =>
                            history.push(`/edit/option/${id}/${option.id}`)
                          }
                        >
                          E
                        </button>
                        <button
                          className="btn btn-danger btn-sm"
                          onClick={() => handleDeleteConfirmation(option.id)}
                        >
                          D
                        </button>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        </>
      )}
    </Template>
  );
};

export default EditMenu;
