import axios from 'axios'
import Cookies from 'js-cookie'

export default axios.create({
  baseURL: '/admin',
  timeout: 5000,
  headers: {
    'Content-Type': 'application/json',
    'X-CSRFToken': Cookies.get('csrftoken')
  }
})