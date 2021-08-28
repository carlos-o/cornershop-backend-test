import { useContext } from "react";

import { DispatcherContext } from "../components/Dispatcher";

export default function useDispatcher() {
  return useContext(DispatcherContext);
}
