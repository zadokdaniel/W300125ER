import { useEffect, useState } from "react";

import "./App.css";

function App() {
  const [data, setData] = useState();
  const [error, setError] = useState();

  useEffect(() => {
    fetch("http://localhost:5000/api")
      .then((response) => response.json())
      .then(setData)
      .catch((error) => setError(error.message));
  });

  return (
    <>
      <h1>Hello from React</h1>

      {error && <p>{error}</p>}
      {data && <pre>{JSON.stringify(data, null, 2)}</pre>}
    </>
  );
}

export default App;
