import { useEffect, useState } from "react";

import "./App.css";

function App() {
  const [data, setData] = useState();
  const [error, setError] = useState();

  useEffect(() => {
    const controller = new AbortController();

    fetch("http://localhost/api", { signal: controller.signal })
      .then((response) => response.json())
      .then(setData)
      .catch((error) => setError(error.message));

    return () => controller.abort();
  }, []);

  return (
    <>
      <h1>Hello from React</h1>

      {error && <p>{error}</p>}
      {data && <pre>{JSON.stringify(data, null, 2)}</pre>}
    </>
  );
}

export default App;
