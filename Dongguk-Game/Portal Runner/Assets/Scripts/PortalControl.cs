using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PortalControl : MonoBehaviour
{
    public static PortalControl portalControlInstance;

    [SerializeField]
    private GameObject aPortal, bPortal;

    [SerializeField]
    private Transform aPortalSpawnPoint, bPortalSPawnPoint;

    private Collider2D aPortalCollider, bPortalCollider;

    [SerializeField]
    private GameObject clone;


    // Start is called before the first frame update
    void Start()
    {
        portalControlInstance = this;
        aPortalCollider = aPortal.GetComponent<Collider2D>();
        bPortalCollider = bPortal.GetComponent<Collider2D>();
    }

    public void CreateClone(string whereToCreate)
    {
        if (whereToCreate == "atA")
        {
            var instantiatedClone = Instantiate(clone, aPortalSpawnPoint.position, Quaternion.identity);
            instantiatedClone.gameObject.name = "Clone"; 
        }
        else if (whereToCreate == "atB")
        {
            var instantiatedClone = Instantiate(clone, bPortalSPawnPoint.position, Quaternion.identity);
            instantiatedClone.gameObject.name = "Clone";
        }
    }

    public void DisableCollider(string colliderToDisable)
    {
        if (colliderToDisable == "a")
        {
            aPortalCollider.enabled = false;
        }
        else if (colliderToDisable == "b")
        {
            bPortalCollider.enabled = false;
        }
    }

    public void EnableColliders()
    {
        bPortalCollider.enabled = true;
        aPortalCollider.enabled = true;
    }
}
