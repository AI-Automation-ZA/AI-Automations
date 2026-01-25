'use client';

import { ReactNode, useEffect, useState } from 'react';
import { useRouter, usePathname } from 'next/navigation';
import {
    LayoutDashboard,
    Users,
    Settings,
    LogOut,
    ChevronRight,
    ShieldCheck,
    Menu,
    X,
    PieChart
} from 'lucide-react';
import { cn } from '@/lib/utils';
import api from '@/lib/api';

interface NavItemProps {
    href: string;
    icon: any;
    label: string;
}

function NavItem({ href, icon: Icon, label }: NavItemProps) {
    const pathname = usePathname();
    const isActive = pathname === href;

    return (
        <a
            href={href}
            className={cn(
                "flex items-center gap-3 px-4 py-3 rounded-xl transition-all group",
                isActive
                    ? "bg-blue-600 text-white shadow-lg shadow-blue-500/20"
                    : "text-slate-400 hover:bg-slate-800 hover:text-white"
            )}
        >
            <Icon className={cn("w-5 h-5", isActive ? "text-white" : "group-hover:text-blue-400")} />
            <span className="font-medium">{label}</span>
            {isActive && <ChevronRight className="ml-auto w-4 h-4 text-white/50" />}
        </a>
    );
}

export default function DashboardLayout({ children }: { children: ReactNode }) {
    const [isSidebarOpen, setIsSidebarOpen] = useState(true);
    const [user, setUser] = useState<any>(null);
    const router = useRouter();

    useEffect(() => {
        const fetchUser = async () => {
            try {
                const response = await api.get('/users/me');
                setUser(response.data);
            } catch (err) {
                router.push('/login');
            }
        };
        fetchUser();
    }, [router]);

    const handleLogout = () => {
        localStorage.removeItem('token');
        router.push('/login');
    };

    return (
        <div className="min-h-screen bg-slate-950 flex text-slate-100">
            {/* Sidebar */}
            <aside className={cn(
                "fixed inset-y-0 left-0 z-50 w-64 bg-slate-900 border-r border-slate-800 transition-transform duration-300 lg:static lg:translate-x-0",
                !isSidebarOpen && "-translate-x-full"
            )}>
                <div className="flex flex-col h-full p-6">
                    <div className="flex items-center gap-3 mb-10 px-2">
                        <div className="w-10 h-10 rounded-xl bg-blue-600 flex items-center justify-center shadow-lg shadow-blue-500/20">
                            <ShieldCheck className="w-6 h-6 text-white" />
                        </div>
                        <span className="text-xl font-bold tracking-tight">Secure CRM</span>
                    </div>

                    <nav className="flex-1 space-y-2">
                        <NavItem href="/dashboard" icon={LayoutDashboard} label="Dashboard" />
                        <NavItem href="/accounts" icon={Users} label="Accounts" />
                        <NavItem href="/pipeline" icon={PieChart} label="Pipeline" />
                        <NavItem href="/settings" icon={Settings} label="Settings" />
                    </nav>

                    <div className="mt-auto pt-6 border-t border-slate-800">
                        <div className="flex items-center gap-3 mb-6 px-2">
                            <div className="w-10 h-10 rounded-full bg-slate-800 flex items-center justify-center border border-slate-700">
                                <span className="text-sm font-bold text-blue-400">
                                    {user?.username?.substring(0, 2).toUpperCase() || 'AD'}
                                </span>
                            </div>
                            <div className="flex-1 overflow-hidden">
                                <p className="text-sm font-semibold truncate">{user?.full_name || 'Admin User'}</p>
                                <p className="text-xs text-slate-500 truncate">{user?.username || 'admin'}</p>
                            </div>
                        </div>
                        <button
                            onClick={handleLogout}
                            className="w-full flex items-center gap-3 px-4 py-3 text-slate-400 hover:text-red-400 hover:bg-red-400/10 rounded-xl transition-all group"
                        >
                            <LogOut className="w-5 h-5 group-hover:scale-110 transition-transform" />
                            <span className="font-medium">Logout</span>
                        </button>
                    </div>
                </div>
            </aside>

            {/* Main Content */}
            <main className="flex-1 flex flex-col min-w-0 overflow-hidden">
                {/* Header */}
                <header className="h-16 border-b border-slate-800 flex items-center justify-between px-8 bg-slate-900/50 backdrop-blur-xl">
                    <button
                        className="lg:hidden text-slate-400 hover:text-white"
                        onClick={() => setIsSidebarOpen(!isSidebarOpen)}
                    >
                        {isSidebarOpen ? <X /> : <Menu />}
                    </button>
                    <div className="flex items-center gap-4">
                        <div className="hidden sm:flex items-center gap-2 px-3 py-1 bg-green-500/10 border border-green-500/20 rounded-full">
                            <div className="w-2 h-2 rounded-full bg-green-500 animate-pulse" />
                            <span className="text-[10px] font-bold text-green-400 uppercase tracking-wider">System Live</span>
                        </div>
                    </div>
                </header>

                {/* Page Area */}
                <div className="flex-1 overflow-y-auto p-8">
                    <div className="max-w-7xl mx-auto animate-in fade-in slide-in-from-bottom-4 duration-500">
                        {children}
                    </div>
                </div>
            </main>
        </div>
    );
}
