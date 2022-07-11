import axios from 'axios';

const API = 'http://localhost:8000';

const getVegetables = () => axios.get(`${API}/vegetables/`)
    .then((res) => ({ response: res, result: true }))
    .catch((err) => ({ response: err, result: false })
);


export { getVegetables };