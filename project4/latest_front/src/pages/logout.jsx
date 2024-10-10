
export function Logout(){
    localStorage.removeItem('authToken');
    localStorage.removeItem('userId');
    window.location.href = `/all_posts`;
}
