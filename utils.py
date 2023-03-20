def group_particles(df, particle_type):
    type_df=df.loc[df["type"]==particle_type]
    df1 = df.groupby("particle type")
    df2 = df1.get_group(type_df)
    print("number of {} particles = {}".format(particle_type, df2.shape[0]))
    return df2

def make_scatter(fig, df, particle_type, parameter_1, parameter_2):
    ax1.scatter(particle_type['parameter 1'], particle_type['parameter 2'], s=0.1, label="particle_type")

    # return the particle type group with the size of the group
# fig=plt.figure(figsize=(20,40))
# ax1=fig.add_subplot(1,1,1)
# for every particle type
    # make a plot against "parameter1", "parameter 2", onto defined figure, particle type
# data locate: 


 # fig=plt.figure(figsize=(20,40))
    #ax1=fig.add_subplot(1,1,1)