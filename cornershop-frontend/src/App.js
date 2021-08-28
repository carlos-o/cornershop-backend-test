import React from "react";
import { BrowserRouter, Switch, Route } from "react-router-dom";

import Auth from "./views/Auth";
import Account from "./views/Account";

import { UserContext } from "./components/User";
import { DispatcherContext } from "./components/Dispatcher";
import CreateMenu from "./views/CreateMenu";
import DetailMenu from "./views/DetailMenu";
import CreateOption from "./views/CreateOption";
import EditOption from "./views/EditOption";
import ViewMenu from "./views/ViewMenu";
import Orders from "./views/Orders";

export default function App() {
  const [user, setUser] = React.useState({
    user: null,
    isLoading: false,
  });

  return (
    <React.Fragment>
      <BrowserRouter>
        <Switch>
          <UserContext.Provider value={user}>
            <DispatcherContext.Provider value={setUser}>
              <Route component={Auth} exact path="/" />
              <Route component={Account} exact path="/account" />
              <Route component={CreateMenu} exact path="/create/menu" />
              <Route component={CreateOption} exact path="/create/option/:id" />
              <Route
                component={EditOption}
                exact
                path="/edit/option/:id/:option"
              />
              <Route component={DetailMenu} exact path="/detail/:id" />
              <Route component={DetailMenu} exact path="/edit/detail/:id" />
              <Route component={ViewMenu} exact path="/menu/:uuid" />
              <Route component={Orders} exact path="/orders" />
            </DispatcherContext.Provider>
          </UserContext.Provider>
        </Switch>
      </BrowserRouter>
    </React.Fragment>
  );
}
