'use client';

import { useEffect, useState } from 'react';
import DashboardLayout from '@/components/layout/DashboardLayout';
import api from '@/lib/api';
import {
    Building2,
    Package,
    TrendingUp,
    type LucideIcon,
    ArrowUpRight,
    ArrowDownRight,
    Briefcase,
    PieChart,
    ShieldCheck
} from 'lucide-react';
import { cn } from '@/lib/utils';

interface DashboardStats {
    total_accounts: number;
    total_products: number;
    total_revenue_won: number;
    total_deals_engaging: number;
}

interface StatCardProps {
    title: string;
    value: string | number;
    icon: LucideIcon;
    trend?: string;
    isPositive?: boolean;
}

function StatCard({ title, value, icon: Icon, trend, isPositive }: StatCardProps) {
    return (
        <div className="bg-slate-900 border border-slate-800 p-6 rounded-2xl group hover:border-blue-500/50 transition-all shadow-xl">
            <div className="flex items-start justify-between">
                <div className="w-12 h-12 rounded-xl bg-slate-800 flex items-center justify-center text-blue-500 group-hover:scale-110 transition-transform">
                    <Icon className="w-6 h-6" />
                </div>
                {trend && (
                    <div className={cn(
                        "flex items-center gap-1 text-xs font-bold px-2 py-1 rounded-lg",
                        isPositive ? "text-green-400 bg-green-400/10" : "text-red-400 bg-red-400/10"
                    )}>
                        {isPositive ? <ArrowUpRight className="w-3 h-3" /> : <ArrowDownRight className="w-3 h-3" />}
                        {trend}
                    </div>
                )}
            </div>
            <div className="mt-4">
                <h3 className="text-slate-400 text-sm font-medium">{title}</h3>
                <p className="text-2xl font-bold mt-1 text-white tracking-tight">{value}</p>
            </div>
        </div>
    );
}

export default function DashboardPage() {
    const [stats, setStats] = useState<DashboardStats | null>(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const fetchStats = async () => {
            try {
                const response = await api.get('/dashboard');
                setStats(response.data);
            } catch (err) {
                console.error('Failed to fetch stats', err);
            } finally {
                setLoading(false);
            }
        };
        fetchStats();
    }, []);

    if (loading) {
        return (
            <DashboardLayout>
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 animate-pulse">
                    {[1, 2, 3, 4].map((i) => (
                        <div key={i} className="h-32 bg-slate-900 border border-slate-800 rounded-2xl" />
                    ))}
                </div>
            </DashboardLayout>
        );
    }

    const formatCurrency = (val: number) => {
        return new Intl.NumberFormat('en-US', {
            style: 'currency',
            currency: 'USD',
            maximumFractionDigits: 0
        }).format(val);
    };

    return (
        <DashboardLayout>
            <div className="mb-8">
                <h1 className="text-4xl font-bold text-white tracking-tight">Business Overview</h1>
                <p className="text-slate-400 mt-2">Real-time insights from your fictitious sales data.</p>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-10">
                <StatCard
                    title="Total Accounts"
                    value={stats?.total_accounts || 0}
                    icon={Building2}
                    trend="+12%"
                    isPositive={true}
                />
                <StatCard
                    title="Total Products"
                    value={stats?.total_products || 0}
                    icon={Package}
                />
                <StatCard
                    title="Revenue (WON)"
                    value={formatCurrency(stats?.total_revenue_won || 0)}
                    icon={TrendingUp}
                    trend="+8.2%"
                    isPositive={true}
                />
                <StatCard
                    title="Engaging Deals"
                    value={stats?.total_deals_engaging || 0}
                    icon={Briefcase}
                    trend="-2%"
                    isPositive={false}
                />
            </div>

            <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
                {/* Placeholder for charts/recent activity */}
                <div className="lg:col-span-2 bg-slate-900 border border-slate-800 rounded-2xl p-8 shadow-xl">
                    <div className="flex items-center justify-between mb-6">
                        <h2 className="text-xl font-bold text-white">Sales Pipeline Distribution</h2>
                        <button className="text-sm text-blue-500 hover:text-blue-400 font-medium transition-colors underline decoration-blue-500/30 underline-offset-4">View Full Report</button>
                    </div>
                    <div className="h-[300px] flex items-center justify-center border-2 border-dashed border-slate-800 rounded-xl bg-slate-800/20">
                        <div className="text-center">
                            <PieChart className="w-12 h-12 text-slate-700 mx-auto mb-3" />
                            <p className="text-slate-500 font-medium">Pipeline visualization coming soon...</p>
                        </div>
                    </div>
                </div>

                <div className="bg-slate-900 border border-slate-800 rounded-2xl p-8 shadow-xl">
                    <h2 className="text-xl font-bold text-white mb-6">Recent Security Logs</h2>
                    <div className="space-y-4">
                        {[1, 2, 3].map((i) => (
                            <div key={i} className="flex gap-4 p-4 rounded-xl bg-slate-800/50 border border-slate-800">
                                <div className="w-10 h-10 rounded-lg bg-blue-500/10 flex items-center justify-center text-blue-400 shrink-0">
                                    <ShieldCheck className="w-5 h-5" />
                                </div>
                                <div>
                                    <p className="text-sm font-medium text-slate-200">Admin login successful</p>
                                    <p className="text-xs text-slate-500 mt-1">IP: 127.0.0.1 • 10m ago</p>
                                </div>
                            </div>
                        ))}
                    </div>
                </div>
            </div>
        </DashboardLayout>
    );
}
