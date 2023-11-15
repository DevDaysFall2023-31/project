import '../styles/App.css';

export const Header = () => {
  return (
    <header className="header block container">
      <span className="logo">Слышно и точка.</span>
      <nav className="menu">
        <a href="#">Избраннное</a>
        <a href="#">Настройки</a>
        <a href="#" className="avatar">
          <img src="https://img.freepik.com/premium-vector/flat-instagram-icons-notifications_619991-50.jpg?size=626&ext=jpg" alt="avatar" />
        </a>
      </nav>
    </header>
  )
}
