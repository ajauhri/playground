//For reference look here - http://stackoverflow.com/questions/1438842/iterating-through-a-lua-table-from-c 
#include<iostream>
#include<stdio.h>
extern "C"
{ 
#include<lua5.2/lua.h>
#include<lua5.2/lauxlib.h>
#include<lua5.2/lualib.h>

}

using namespace std;

static int load_platform(lua_State *L)
{
	const char *file = lua_tostring (L, 1);
	std::cout << "load platform: " << file << endl;
	return 0;
}

static int add_antenna(lua_State *L)
{
	const char *file = lua_tostring (L, 1);
	std::cout << "load antenna: " << file << endl;
	return 0;
}

static int add_point(lua_State *L)
{
	double x = lua_tonumber (L, 1);
	double y = lua_tonumber (L, 2);
	double z = lua_tonumber (L, 3);
	std::cout<<"x="<<x<<"y="<<y<<"z="<<z<<"\n";
	return 0;
}

int main() 
{
	std::cout<<"starting\n";
	lua_State *L = luaL_newstate();
	luaL_openlibs(L);

	lua_pushcclosure (L, load_platform, 0);
	lua_setglobal (L, "load_platform");

	lua_pushcclosure (L, add_antenna, 0);
	lua_setglobal (L, "add_antenna");

	lua_pushcclosure (L, add_point, 0);
	lua_setglobal (L, "add_point");

	luaL_dofile(L, "test_1.lua");

	lua_getglobal(L, "params");
	lua_pushnil(L);
	while(lua_next(L, -2) != 0)
	{
		if (lua_isnumber(L, -1)) 
		{
			std::cout<<lua_tostring(L, -2)<<" "<<lua_tonumber(L, -1)<<"\n";
			lua_pop(L, 1);
		}
		else
		{
			std::cout<<lua_tostring(L, -2)<<" "<<lua_tostring(L, -1)<<"\n";
			lua_pop(L, 1);
		}

	}
	lua_pop(L, 1);
	lua_close(L);
	return 0;
}




