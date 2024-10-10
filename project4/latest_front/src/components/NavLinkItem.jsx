import { NavLink } from 'react-router-dom';

const NavLinkItem = ({ to, children }) => {
  return (
    <div className="mx-2">
        <NavLink
        to={to}
        className="text-xl font-bold p-0 pb-4"
        //activeClassName="text-gray-400" // Optional: Tailwind-specific
        >
        {children}
        </NavLink>
    </div>
  );
};

export default NavLinkItem;
